// Copyright 2015-2019 VMware, Inc. All Rights Reserved.
// Author: Tom Hite (thite@vmware.com)
//
// SPDX-License-Identifier: https://spdx.org/licenses/MIT.html
//
package app

import (
	"net/url"
	"testing"
)

func TestGoReminders(t *testing.T) {
	if testing.Short() {
		t.Skip("Skipping: short mode ignores tests.")
		return
	}

	Init()
	//t.Log("Package app tested ok.")
	//t.Error("Expected Success or Fail, got ")

	// Test for URL correctness returned from
	// getUrlRoot() function in realmain.go
	testVHost := getUrlRoot()
	t.Log("Returned from function is ", testVHost)
	u, err := url.ParseRequestURI(testVHost)
	if err != nil {
		t.Error(err)
	} else {
		t.Log("URL is good", u)
	}

}
